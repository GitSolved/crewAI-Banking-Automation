#!/usr/bin/env python
import sys
from employer_branding.crew import EmployerBrandingCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'customer_domain': 'alpinecapitalbank.com',
        'project_description': """
Alpine Capital Bank, a premier financial services institution, aims to enhance its employer branding and talent acquisition efforts. This project involves developing an innovative marketing strategy to showcase Alpine Capital Bank's career opportunities, workplace culture, and professional development programs. The campaign will target experienced banking professionals and recent graduates, highlighting success stories and the growth potential within Alpine Capital Bank's organization.

Customer Domain: Banking and Financial Services
Project Overview: Creating a comprehensive employer branding campaign to boost awareness and attract top talent to Alpine Capital Bank's various departments.
"""
    }
    EmployerBrandingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer_domain': 'alpinecapitalbank.com',
        'project_description': """
Alpine Capital Bank, a premier financial services institution, aims to enhance its employer branding and talent acquisition efforts. This project involves developing an innovative marketing strategy to showcase Alpine Capital Bank's career opportunities, workplace culture, and professional development programs. The campaign will target experienced banking professionals and recent graduates, highlighting success stories and the growth potential within Alpine Capital Bank's organization.

Customer Domain: Banking and Financial Services
Project Overview: Creating a comprehensive employer branding campaign to boost awareness and attract top talent to Alpine Capital Bank's various departments.
"""
    }
    try:
        EmployerBrandingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
