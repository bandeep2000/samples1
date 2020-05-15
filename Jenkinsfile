pipeline {
    agent any
    environment {
       
       DOCKER_PASSWD = credentials('docker-passwd')
       GIT_PASSWD    = credentials('github-passwd')
       //GIT_SHA = sh '`git log -1 --pretty=%h`'
    }
    //agent {
    //    docker { image 'node:7-alpine' }
    //}
     //parameters {
    //  string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    //}
    stages {
        stage('test local') {
            agent {docker 'bandeep2000/python' }
            steps {
               
               withEnv(["PATH_BIN=/var/jenkins_home/.local/bin"]) {
                
                sh 'env'
                
                sh 'python -m pytest -v isReverse.py --junitxml=path'
                junit 'path'
                
                sh 'python  isReverse.py'
                
               }
            }
        }

        stage('Build Image') {
            steps {

                sh 'docker ps'
                sh 'docker build -t bandeep2000/python-test:`git log -1 --pretty=%h` .'

                script {
                    sh "git log -1 --pretty=%h > commandResult"
                    def result = readFile('commandResult').trim()
                    echo "${result}"

                    sh "docker build -t bandeep2000/python-test:${result} ."
                    //sh "sed \"s/COMMIT_SHA/${result}/g\" test1.yml.tpl > test1.yml"
                  
                  }    
                 
            }
        }

        stage('Test and push Image') {
            steps {
                
                script {
                    def result = readFile('commandResult').trim()
                    echo "${result}"
                    sh "docker run --rm  bandeep2000/python-test:${result} python -m pytest isReverse.py"
                    sh "docker login -u bandeep2000 -p  $DOCKER_PASSWD"
                    sh "docker push bandeep2000/python-test:${result}"
                }
            }
        }
        stage('Push Kube Manifest') {
            steps {

              //checkout kube branch
              git branch: 'kube',credentialsId: '22cea117-6a3d-42ba-8e99-1a654c5ba61a', url: 'https://github.com/bandeep2000/kubernetes-ban.git'
              //set git variables
              sh 'git config --global user.email "bandeep2000@gmail.com"'
              sh  'git config --global user.name "bandeep2000"'
              dir('centos-samples') {
                            
                  script {
                    //sh "git log -1 --pretty=%h > commandResult"
                    def result = readFile('../commandResult').trim()
                    echo "${result}"
                    sh "sed \"s/COMMIT_SHA/${result}/g\" test1.yml.tpl > test1.yml"
                    sh 'git add test1.yml'
                    sh "git commit -m \"modfied kubernetes manifest with SHA ID ${result}\""
                    //set this otherwise git push doesn't work
                    sh "git remote set-url origin https://bandeep2000:$GIT_PASSWD@github.com/bandeep2000/kubernetes-ban.git"
                    //commit to kube branch
                    sh 'git push origin kube'
                  
                  }    
    
              }
              
              
              
              
            }

        }
          
    }
}
