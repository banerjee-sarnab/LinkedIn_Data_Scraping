from linkedin_api import Linkedin
from constants import LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASS

api = Linkedin(LINKEDIN_USER_EMAIL, LINKEDIN_USER_PASS)

# profile = api.get_profile('sarnab-banerjee-28a9a5223')

profile = api.search(params={'keywords': 'Debraj Chatterjee'}, limit=5)

print(len(profile))