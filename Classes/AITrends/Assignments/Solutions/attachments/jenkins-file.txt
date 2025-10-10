pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build process'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy'
            }
        }
        stage('Test') {
            steps {
                echo 'testing'
            }
        }
    }
}
===========================================================================================================================


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/saruti1/repo.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/saruti1/repo.git'
                bat 'python helloworld.py'
            }
        }
        stage('Test') {
            steps {
                echo 'TESTING'
            }
        }
    }
}
========================================================================================================

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/saruti1/repo.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/saruti1/repo.git'
                bat 'python helloworld.py'
            }
        }
        stage('Test') {
            steps {
                echo 'TESTING'
            }
        }
         stage('Docker Deploy') {
            steps {
                echo 'Building Docker image...'
                // Build Docker image (tag as 'myapp:latest')
                bat 'docker build -t myapp:latest .'

                echo 'Running Docker container...'
                // Run Docker container on port 5000
                bat 'docker run -d --name myapp_container11 myapp:latest'

                echo 'Docker deployment completed!'
            }
        }
    }
}
================================================================================================================================S