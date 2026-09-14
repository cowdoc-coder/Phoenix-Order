# Phoenix Dairy — Animal Health Order Form

An order form (desktop + phone) that sends the order to Johnny Williams as a
real SMS. It runs entirely on GitHub, the same way the Homeland VETCHECK
pipeline does:

- **GitHub Pages** hosts the form (`index.html`).
- **GitHub Actions** does the sending (`send-order.yml` → `send_order.py`),
  with the Twilio credentials stored as encrypted **Actions Secrets**.
- The form triggers the Action on demand using a small per-device token.

The text to Johnny is **always built in English**, regardless of the screen
language (EN/ES toggle only changes what the user sees).

---

## One-time setup

### 1. Create the repo and upload these files
Create a repo (e.g. `phoenix-order`) and upload, keeping the folders:
```
index.html
send_order.py
requirements.txt
.github/workflows/send-order.yml
```

### 2. Add the Twilio credentials as Actions Secrets
Repo → **Settings → Secrets and variables → Actions → New repository secret**.
Add these four (same Twilio account you use for the breeding texts):

| Secret name           | Value                                   |
|-----------------------|-----------------------------------------|
| `TWILIO_ACCOUNT_SID`  | Your Twilio Account SID                 |
| `TWILIO_AUTH_TOKEN`   | Your Twilio Auth Token                  |
| `TWILIO_FROM`         | Your Twilio phone number, e.g. `+1559...`|
| `ORDER_TO`            | Johnny's number: `+15592176778`         |

These live server-side and are never exposed to the browser.

### 3. Point the form at your repo
Edit the top of the `<script>` in `index.html`:
```js
const GH_OWNER = "cowdoc-coder";
const GH_REPO  = "Phoenix-Order";
```
Commit the change.

### 4. Turn on GitHub Pages
Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / root → Save.
After ~1 minute it gives you the URL: `https://YOUR_USERNAME.github.io/phoenix-order/`

### 5. Create the device "send token"
This is what lets the form trigger the Action.
**GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token:**
- **Repository access:** only the `phoenix-order` repo
- **Permissions:** Repository permissions → **Contents: Read and write**
- Copy the token (starts with `github_pat_...`).

### 6. Open it and enter the token once
Open the Pages URL on the desktop (and/or Eric's phone). The first time you
press **Send**, it asks for the token — paste it. It's stored in that device's
browser only and reused after that. (It is **not** in the code or the repo.)

---

## Daily use
Set quantities (or add products at the bottom), press **Send the order
to Johnny**. The Action fires and Johnny gets the SMS within a few seconds.
The order resets so the next one starts clean. Products you add stay on the
list (this device immediately; every device after GitHub Pages refreshes).

- **Add to Home Screen** on a phone for an app-like icon (Share → Add to Home
  Screen on iPhone; ⋮ → Add to Home screen on Android).
- The **EN/ES** toggle is remembered per device until someone switches it back.
- The copy button (⧉) is a manual backup that copies the order text.

## Updating the product list
Use **+ Add another product** on the form. Added products are saved and shown
in alphabetical order. Removing a product (the × under a saved extra) drops it
from the saved list too.

You can still edit the `BASE` list in `index.html` and commit if you want to
change the built-in catalog in the source.

## Security note
The Twilio keys are safe in Actions Secrets. The per-device send token can
trigger this one repo's workflow, so treat it like an internal password and use
a private repo if you'd rather not expose the form/source publicly (GitHub Pages
on a private repo requires GitHub Pro). To revoke a device, delete the
fine-grained token in GitHub and it stops working immediately.
