#!/usr/bin/env python
import sys
from resume_job_matcher.crew import ResumeJobMatcherCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'path_to_jobs_csv': './src/resume_job_matcher/data/jobs.csv',
        'path_to_cv': './src/resume_job_matcher/data/cv.md'
    }
    ResumeJobMatcherCrew().crew().kickoff(inputs=inputs)

