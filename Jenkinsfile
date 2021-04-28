pipeline {
    environment {
    PATH="/var/lib/jenkins/miniconda3/bin:$PATH"
  }
    agent none 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps {
                sh '''conda create --yes -n ${BUILD_TAG} python
                      source activate ${BUILD_TAG} 
                      pip install -r requirements.txt
                    '''
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
                sh 'python unittest_blackjack.py'
                sh 'python integrationtest_blackjack.py'
                sh  ''' source activate ${BUILD_TAG}
                        coverage run unittest_blackjack.py integratontest_blackjack.py
                        python -m coverage xml -o ./reports/coverage.xml
                    '''
            }
        }
        stage('Deploy'){
            steps{
                script {
                    docker.withRegistry('https://580378872946.dkr.ecr.us-east-2.amazonaws.com/blackjack-python',
                    'ecr:us-east-2:my.aws.credentials') {
                        def myImage = docker.build('blackjack-python')
                        myImage.push('latest')
                    }
                }
            }
        }
    }
}