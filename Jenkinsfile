pipeline {
    environment {
    registry = "jazelyn/blackjack-python"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
    agent none 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile card.py deck.py person.py dealer.py player.py blackjack.py' 
                stash(allowEmpty: false, name: 'compiled-results', includes: 'card.pyc,deck.pyc,person.pyc,dealer.pyc,player.pyc,blackjack.pyc') 
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python unittest_blackjack.py'
                sh 'python integrationtest_blackjack.py'
            }
        }
        stage('Deploy'){
            agent {
                docker { image 'node:latest' }
            }
            steps{
                script {
                    docker.withRegistry('https://580378872946.dkr.ecr.us-east-2.amazonaws.com/blackjack-python',
                    'ecr:us-east-2:my.aws.credentials') {
                        def myImage = docker.build('blackjack-python')
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}