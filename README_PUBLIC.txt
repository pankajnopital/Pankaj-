PUBLIC DEPLOY PACKAGE — PUNDHIR'S CCTV SERVICES

Folder structure:
app.py
requirements.txt
static/
  gallery1.jpg
  gallery2.jpg
  gallery3.jpg
  gallery4.jpg

Deploy on Render:
Build command: pip install -r requirements.txt
Start command: gunicorn app:app

Important:
- Upload the CONTENTS of this folder to the top level of your GitHub repository.
- Keep the static folder beside app.py; do not rename it.
- The free Render web service can sleep after 15 minutes idle and may take about a minute to wake.
- Do not publish private customer/site photos without permission.
