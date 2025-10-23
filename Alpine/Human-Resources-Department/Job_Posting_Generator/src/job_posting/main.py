import sys
from job_posting.crew import JobPostingCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'company_domain':'careers.alpinecapitalbank.com',
        'company_description': "Alpine Capital Bank is a premier financial services institution offering comprehensive banking solutions including retail banking, wealth management, commercial lending, and investment services. We're committed to delivering exceptional client experiences through innovative financial products and personalized service.",
        'hiring_needs': 'Senior Financial Analyst, for our Corporate Finance division in New York starting Q2 2025',
        'specific_benefits':'Competitive Salary, 401(k) Matching, Health Insurance, Professional Development, Performance Bonuses',
    }
    JobPostingCrew().crew().kickoff(inputs=inputs)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'company_domain':'careers.alpinecapitalbank.com',
        'company_description': "Alpine Capital Bank is a premier financial services institution offering comprehensive banking solutions including retail banking, wealth management, commercial lending, and investment services. We're committed to delivering exceptional client experiences through innovative financial products and personalized service.",
        'hiring_needs': 'Senior Financial Analyst, for our Corporate Finance division in New York starting Q2 2025',
        'specific_benefits':'Competitive Salary, 401(k) Matching, Health Insurance, Professional Development, Performance Bonuses',
    }
    try:
        JobPostingCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
