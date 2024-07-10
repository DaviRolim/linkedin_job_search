#!/usr/bin/env python
import sys
from linkedin_job_search.crew import LinkedinJobSearchCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'applicant_resume': """
        profile:
  summary: >
    Software engineer with vast experience designing cloud architectures (12x AWS Certified). 
    Experience with building solutions using a broad set of AWS services and best-practices. 
    Capable of developing, testing, and maintaining web applications. 
    Experience with CI/CD pipelines, relational and NoSQL databases, and Git. 
    Always excited to learn new technologies, currently interested in building AI applications.
  linkedin: "https://www.linkedin.com/in/davi-rolim-9a489b11b/"

employment_history:
  - position: Sr. Software Engineer
    company: Nubank
    location: São Paulo
    duration: January 2022 — Present
    responsibilities: |
      - Working as a full cycle developer on BDC (Backend Driven Content).
      - Participating in scrum meetings.
      - Writing backend code using Clojure.
      - Writing mobile code using Flutter.
      - Interacting with CI/CD pipelines.
      - Applying critical thinking to help prioritize next features.
      - Pair programming.
      - Writing technical documentation.

  - position: Solutions Architect
    company: Amazon Web Services
    location: São Paulo
    duration: March 2020 — December 2021
    responsibilities: |
      - Assisting customers of manufacturing segment with diverse cloud workloads, building resilient and secure architectures, also reducing time to market.
      - Developing solutions using serverless technologies such as AWS Lambda, Amazon API Gateway, AWS Step Functions, mainly using Python.
      - Using Infrastructure as Code with AWS CDK (Cloud Development Kit).
      - Assisting customers in application modernization, from monolith to microservices.

  - position: Software Developer
    company: MV Sistemas
    location: Recife
    duration: December 2016 — January 2020
    responsibilities: |
      - Worked as a full-stack developer, mainly using Java in the back-end and JavaScript (VueJs) on the front-end.
      - Building a healthcare product used by hundreds of users.
      - Developing solutions using serverless technologies such as AWS Lambda, Amazon API Gateway, AWS Step Functions, mainly using Python.
      - Using Infrastructure as Code with AWS CDK (Cloud Development Kit).
      - Assisting customers in application modernization, from monolith to microservices.
      - Helping new developers who joined the team, becoming a point of reference within the team.
      - Reducing costs of architecture of a cron Job critical to the project’s operation, by replacing a fleet of EC2 machines with a lambda function.

  - position: Developer Intern
    company: Fábrica de Software Unipê
    location: João Pessoa
    duration: September 2016 — November 2016
    responsibilities: |
      - Working as a developer building new features for their web portal.
      - Developing web applications using Django Framework.
      - Version control with GitHub.

freelance:
  - position: Front-end Developer
    company: MybetSpace
    location: Cabedelo
    duration: September 2021 — December 2021
    responsibilities: |
      - Working as a freelancer for MybetSpace building new features for their front-end.
      - Using VueJs for front-end development.
      - Server-side rendering with Nuxt.
      - Version Control with GitHub.
      - Using Docker to interact with the backend.

education:
  - degree: BS in Computer Science
    institution: University of Guararapes (UNIFG)
    location: Recife
    duration: August 2015 — December 2019

certifications:
  - name: AWS Certified Cloud Practitioner
    year: 2020
  - name: AWS Certified Solutions Architect - Associate
    year: 2020
  - name: AWS Certified SysOps Administrator - Associate
    year: 2020
  - name: AWS Certified Developer - Associate
    year: 2020
  - name: AWS Certified DevOps Engineer - Professional
    year: 2020
  - name: AWS Certified Solutions Architect - Professional
    year: 2020
  - name: AWS Certified Advanced Networking - Specialty
    year: 2021
  - name: AWS Certified Alexa Skill Builder - Specialty
    year: 2020
  - name: AWS Certified Data Analytics - Specialty
    year: 2020
  - name: AWS Certified Database - Specialty
    year: 2020
  - name: AWS Certified Machine Learning - Specialty
    year: 2020
  - name: AWS Certified Security - Specialty
    year: 2020

skills:
  - Flutter
  - Clojure
  - Java
  - JavaScript
  - Python
  - CI/CD
  - Serverless
  - Vue.js
  - Test Driven Development
  - Unit Tests
  - GitHub
  - PostgreSQL
  - Oracle
  - NoSQL

extra_activities:
  - activity: >
      Published blog post in AWS (Portuguese): 
      [Detecting image anomalies with Amazon Lookout for Vision](https://aws.amazon.com/pt/blogs/aws-brasil/detectando-anomalias-em-imagens-com-o-amazon-lookout-for-vision-parte-1/)

        """
    }
    LinkedinJobSearchCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        LinkedinJobSearchCrew().crew().train(
            n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
