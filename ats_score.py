def calculate_ats(resume_skills, job_skills):
    matched = set(resume_skills).intersection(set(job_skills))
    score = (len(matched) / len(job_skills)) * 100
    return round(score, 2), list(matched)
