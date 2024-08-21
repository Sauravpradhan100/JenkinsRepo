pipeline{
    agent any
    stages{
        stage("Checkout Code Stage"){
            steps{
                git url:'https://github.com/Sauravpradhan100/jenkinsrepo.git', branch:'main'
            }
        }
        /*stage("Cleanup Stage"){
            steps{
                sh 'docker rm -f $(docker ps -aq)'
                sh 'docker rmi -f myimage'
            }
        }*/
        stage("Build Docker Image"){
            steps{
                sh 'docker rmi -f myimage .'
            }
        }
        stage('Build and Push Image'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myimage $DOCKER_USERNAME/myimage'
                    sh 'docker push $DOCKER_USERNAME/myimage'
                }
            }
        }
        stage('Kubernetes deployment'){
            steps{
                sh 'kubectl apply -f my-deployment.yml'
            }
        }
    }
}