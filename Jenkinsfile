#!/usr/bin/env groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest tests.appannietests.TestAppAnnie'
            }
        }
        stage('SonarQube') {
            steps {
                echo 'Analyzing code quality....'
            }
        }
    }
}