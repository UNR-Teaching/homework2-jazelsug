pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile card.py deck.py person.py dealer.py player.py blackjack.py' 
                stash(name: 'compiled-results', includes: 'py_compile card.py deck.py person.py dealer.py player.py blackjack.py') 
            }
        }
    }
}