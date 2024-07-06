import assemblyai as aai

#create a transcriber
transcriber = aai.Transcriber()
transcript = transcriber.transcribe("<path_to_file>")

#ai settings
prompt = """
ROLE:
You are a customer service professional. You are very competent and able to \
extract meaningful insights from transcripts of customer calls that are \
submitted to you.
CONTEXT:
THis is a call from somenone who is inquiring at a home building company
INSTRUCTION
Respond to the following command: \
"Provide a short summary of the phone call, and list any outstanding action items \
after the summary. Finally, provide the caller's contact information. Do not \
include a preamble.
FORMAT:
SUMMARY:
a one or two sentence summary
ACTION ITEMS:
a bulleted list of sufficiently detailed action items
CONTACT INFORMATION:
Name: Last name, first name
Phone number: The caller's phone number
""".strip()

#use lemur
result = transcript.lemur.task(prompt)
#remove all white space
print(result.response.strip())
