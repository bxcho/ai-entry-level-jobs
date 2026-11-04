# Holdout: labeled AFTER the last rule change (quote these numbers)
- Postings hand-labeled: **40**
- AI skill, precision (when it says yes, how often you agreed): **80%**
- AI skill, negative agreement (when it says no, how often you agreed): **95%**
- AI skill, accuracy weighted to the real mix of postings: **88%**
- Function accuracy: **90%** (n=40)
- Level accuracy among stored postings: **92%** (n=40)

## Disagreements on AI skill (use these to fix the word lists in classify.py)
- Samsara | Associate Sales Engineer, SE Desk - TOLA | you: no | rule: yes | Become an expert on Samsara products: where the rubber of cutting-edge tech (IoT, AI, computer vision) meets the road of
- Veeva Systems | Associate Consultant - Entry-Level Technology Consulting | you: no | rule: yes | In this role, you’ll learn our industry-leading cloud platforms and work with cutting-edge AI solutions to transform how
- Cloudflare | Business Development Representative - Dutch Speaking | you: no | rule: yes | We value candidates who have the instinct to spot a "normalized" problem and the AI-native curiosity to create a solutio
- Oscar Health | Bilingual Medical Assistant (Part-Time) | you: no | rule: yes | outline the acceptable use of artificial intelligence for candidates and detail how we use AI to support our recruiting 
- Palantir | Software Engineer, New Grad - Production Infrastructure | you: yes | rule: no | 

## Disagreements on level (use these to fix the level rules in classify.py)
years = the largest 'N years of experience' the rules found in the posting
- Samsara | Select Major Account Executive, UK&I | you: other | rule: entry | years: none
- Databricks | Solutions Engineer | you: other | rule: entry | years: 1
- Anthropic | Data Center Asset Management, Commercial Associate | you: other | rule: entry | years: none

## Disagreements on function
- Anthropic | Data Center Asset Management, Commercial Associate | you: legal_policy | rule: data_ml
- Veeva Systems | Technical Customer Service Associate | you: other | rule: consulting_strategy_ops
- Lyft | Business Systems Engineer Intern, Finance Technology (Summer 2027) | you: software_eng | rule: finance_accounting
- Robinhood | Customer Experience Associate, Money | you: other | rule: consulting_strategy_ops

# Tuning set: the labels used to fix the rules (these will look better than reality)
- Postings hand-labeled: **80**
- AI skill, precision (when it says yes, how often you agreed): **98%**
- AI skill, negative agreement (when it says no, how often you agreed): **100%**
- AI skill, accuracy weighted to the real mix of postings: **99%**
- Function accuracy: **99%** (n=80)
- Level accuracy among stored postings: **95%** (n=80)

## Disagreements on AI skill (use these to fix the word lists in classify.py)
- Figma | Technical Quality Specialist - Figma Weave (Singapore) | you: no | rule: yes | Figma’s platform helps teams bring ideas to life—whether you're brainstorming, creating a prototype, translating designs

## Disagreements on level (use these to fix the level rules in classify.py)
years = the largest 'N years of experience' the rules found in the posting
- Datadog | Recruiting Coordinator | you: entry | rule: other | years: 2
- Twilio | Phone Numbers Operations Specialist 1 | you: entry | rule: other | years: 2
- Coinbase | Broker Dealer Operations, Associate | you: other | rule: entry | years: none
- OpenAI | BIM Designer & Coordinator | you: other | rule: entry | years: none

## Disagreements on function
- Veeva Systems | Strategy Associate - Veeva Link | you: sales_marketing | rule: consulting_strategy_ops

