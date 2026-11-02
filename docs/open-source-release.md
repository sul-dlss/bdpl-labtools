# Stanford attribution model: licensing and attributing staff-built open-source software at Stanford Libraries

**Prepared for:** the BDPL design lead and the Stanford Libraries operations manager approving the public release of `sul-dlss/bdpl-labtools-da-capture` (BDPL LabKit)
**Also covers:** `sul-dlss/bdpl-labtools` and `sul-dlss/bdpl-labtools-dedupe` (already public, Apache-2.0, LICENSE template not yet filled in)
**Research date:** 2026-11-01. Every policy claim below is dated; "last updated" is the date shown on the page where one is shown.
**Method:** Stanford policy pages and OTL/UIT pages were fetched directly; sul-dlss LICENSE and README files were fetched from `raw.githubusercontent.com` and the GitHub REST API (161 public repositories), not inferred from GitHub's license badge.

Throughout, three kinds of statement are kept apart:

- **Stanford policy (binding)** — Research Policy Handbook (RPH), Administrative Guide, OTL and UIT pages.
- **sul-dlss convention (observed)** — what the organization's repositories actually contain.
- **Recommendation** — our proposed wording and steps.

---

## 1. Summary of the recommendation

1. **Copyright holder.** Software written by a Stanford staff member as part of the job is University-owned under the RPH Copyright Policy (work-for-hire; significant use of staff programmer time). The copyright line must therefore name the University, not the individual: **"Copyright 2026 The Board of Trustees of the Leland Stanford Junior University."** This is also exactly what sul-dlss repositories use (observed in argo, dor-services-app, exhibits, preservation_catalog, common-accessioning, dlme, sul_pub, SearchWorks).
2. **License.** Apache-2.0, the dominant choice in sul-dlss (28 of 158 live public repos carry a machine-detected Apache-2.0 LICENSE; a further 65 carry a hand-prefixed Apache-2.0 LICENSE that GitHub reports as "Other"). No Stanford policy prescribes a license; OTL's only hard requirement is that Stanford have clear copyright ownership of everything it licenses.
3. **Approval.** There is no published Stanford form or OTL sign-off step for open-sourcing staff-written, unpatentable library software. The best available statement of practice is Tom Cramer (then DLSS) citing OTL's Open Source Primer: staff "may open source software with the appropriate departmental approval" (2015). Treat the operations manager's written approval as that departmental approval, and record it in the repository.
4. **AI attribution.** Stanford has no policy on attributing AI assistance in code. UIT's Responsible AI guidance asks staff to "transparently cite" generative-AI use where permitted and to consider informing people when AI "significantly influences your final product." LabKit's existing practice (a `Co-Authored-By: Claude …` trailer on every commit, plus `PROVENANCE.md`) already exceeds any Stanford expectation and matches the direction of upstream open-source norms (Linux kernel `Assisted-by:`, Fedora/NixOS declaration rules). Keep it; add a short README "Attribution" block and keep the human as the sole accountable author.
5. **Before flipping to public:** fill in the LICENSE copyright line, add NOTICE, scan full git history for secrets and personal data, confirm third-party license compatibility (DEPENDENCIES.md), check the EAR encryption-notification question (LabKit contains an AES-256 license-key component), confirm no Stanford logo or implied-endorsement use, and register the project with OpenSource@Stanford (optional, but gives Stanford a record of the release).

---

## 2. Stanford policy (binding)

### 2.1 Who owns staff-written software

**Source:** Research Policy Handbook, *Copyright Policy*, current version March 18, 2018 (original August 1, 1983). <https://doresearch.stanford.edu/policies/research-policy-handbook/intellectual-property/copyright-policy>

| Provision | What it says | Relevance to LabKit |
|---|---|---|
| §2.C scope | Binds "all faculty, staff, student employees, graduate students and postdoctoral fellows," whether or not an SU-18 Patent and Copyright Agreement is on file. | Michael Olson, as staff, is covered. |
| §2 general rule | Copyright "shall remain with the creator unless the work is a work-for-hire" or another listed exception (institutional work, significant use of University resources or personnel, sponsored-research obligation) applies. | A staff member's job-scope work is a work-for-hire. |
| §1.A | University claims no ownership of *unpatentable software* that is not an institutional work and "did not make significant use of University resources." | Does not help here: LabKit was built during employment, on Stanford business, for a Stanford lab. |
| §2.G | Significant use includes use of "the services of University non-faculty employees"; the creator "shall disclose the work to the Office of Technology Licensing and assign title to the University." Ordinary desktop-computer use is *not* significant use. | Staff programmer time is the paradigm case of significant use. |
| §3.B | Significant use of "staff or student employee programmers" will typically result in "University ownership of the copyright in the resulting work." | Confirms University ownership. |
| §2.H | A creator may ask the Dean of Research to reconvey copyright; granted at the Dean's discretion. | Not needed; University ownership is the desired outcome. |

**Conclusion (policy):** The copyright in LabKit, bdpl-labtools and bdpl-labtools-dedupe belongs to the University. The legal entity is **The Board of Trustees of the Leland Stanford Junior University**, the form used on OTL's own site footer ("© The Board of Trustees of the Leland Stanford Junior University", <https://otl.stanford.edu/software>) and in every sul-dlss LICENSE that names a holder (§3 below). Naming an individual or "Stanford Libraries" as copyright holder would be wrong.

**Patentable software** is governed separately by RPH *Inventions, Patents and Licensing*, current version October 30, 2023: title to inventions by "staff or other employees" is "assigned to the University, regardless of the source of funding," and inventors "must prepare and submit on a timely basis an invention disclosure for each potentially patentable invention" to OTL. <https://doresearch.stanford.edu/policies/research-policy-handbook/intellectual-property/inventions-patents-and-licensing>. LabKit is a workflow application assembling existing open tools (ClamAV, Siegfried/Brunnhilde, BagIt, PREMIS) and is not plausibly patentable; no invention disclosure appears to be required, but this is a judgment call the operations manager can confirm with OTL in one email (otl-information@stanford.edu, listed in a 2020 OTL deck: <https://med.stanford.edu/content/dam/sm/mchri/documents/about/Stanford%20MCHRI%20Webinar_OTL_Non-Confidential_11092020.pdf>).

### 2.2 What OTL says about open source

**Source:** OTL, *Software* page (no date shown). <https://otl.stanford.edu/software>

- "Copyrighted software can be licensed (including through an open source license) to the academic community" and to "the commercial community."
- "To be licensable under any kind of license (including an open source license), Stanford must have clear copyright ownership." "It is responsibility of Stanford creators to ensure that Stanford has rights to software created at Stanford."
- "NOTE: Open source is different from public domain."
- The page names **no preferred license** and **no approval step** for open-source release.

The RPH Copyright Policy itself does not mention open source at all (fetched 2026-11-01). Neither does the Inventions policy, beyond allowing inventors to "place inventions in the public domain if that would be in the best interest of technology transfer" (§2.D).

**The "departmental approval" rule.** The only Stanford statement specifically about staff open-sourcing software that this research located is second-hand: Tom Cramer (then Stanford Libraries / DLSS) wrote on CODE4LIB on January 10, 2015 that OTL's *Open Source Primer* says "Stanford staff may open source software with the appropriate departmental approval," and that DLSS's departmental policy pointed to the Apache 2.0 license instructions. <https://www.mail-archive.com/code4lib@listserv.nd.edu/msg26366.html>. The Primer itself could not be found online in 2026 (see Unverified). A Stanford affiliate page (SUETRI-B) likewise says it "will follow the open source licensing terms prescribed by the Stanford Office of Technology Licensing" when releasing code, implying OTL has such terms. <https://suetri-b.stanford.edu/affiliates/affiliate-resources/software>

**Conclusion (policy + practice):** Stanford has no release form for this class of software. The operative gate is departmental approval, which for the Libraries means the responsible manager. Record it.

### 2.3 OpenSource@Stanford

OpenSource@Stanford describes itself as "the organizational hub that coordinates, facilitates, and supports open source activity at Stanford," now housed in the Stanford Institute for Human-Centered AI after the 2026 HAI/Data Science merger. It offers a **Projects Registry**, workshops, and **consultations on "what licenses to use"**; contact opensource-info@stanford.edu. It publishes no license, notice, release or AI-disclosure guidance of its own. <https://opensource.stanford.edu/> (fetched 2026-11-01). The Sloan Foundation funded "the institutionalization of an Open Source Programs Office at Stanford University" in 2025. <https://sloan.org/grant-detail/g-2025-25270>

**Conclusion:** Not a required step, but registering LabKit in the Projects Registry is the closest thing Stanford has to "a record of the release," and a consult is free if the operations manager wants a second opinion on the license.

### 2.4 Use of the Stanford name and marks

**Source:** Administrative Guide 1.5.4, *Ownership and Use of Stanford Trademarks and Images*, last updated July 25, 2017. <https://adminguide.stanford.edu/chapters/guiding-policies-and-principles/conflict-interest/ownership-and-use-stanford-trademarks>

- Faculty and staff may use Stanford's marks only for activities "officially sponsored or sanctioned by Stanford"; use within normal academic, research and employment activities is allowed under each unit's own review processes.
- Trademark Licensing must be consulted before using marks "on any product, in a book title, in the name of any non-Stanford business or activity," or on merchandise. The policy does not address software by name.
- The Name Use Guidelines (effective March 1, 2014, amended October 2025) add that "school- and unit-level names should be used, unless the activity is an institutional or university-wide endeavor." <https://trademarks.stanford.edu/name-use-guidelines>
- Stanford's own InVEST software shows the institution does register software names as trademarks and polices confusing use. <https://naturalcapitalproject.stanford.edu/software/invest/invest-trademark-and-logo-use-policy>

**Conclusion:** "BDPL LabKit" as a name, and "Stanford Libraries" / "Born-Digital Preservation Lab" as descriptive attribution in a README, are ordinary unit-level use of the name by the unit itself and need no Trademark Licensing review. Do **not** put the Stanford wordmark, seal or tree logo in the repository or app UI, and do not use "Stanford" as part of the product name (e.g. "Stanford LabKit") without asking trademark_licensing@stanford.edu.

### 2.5 Generative-AI guidance

- **UIT, Responsible AI** (no page date): avoid entering "Moderate or High Risk Data" or "proprietary source code" into third-party AI tools not under a Stanford agreement; for content creation, where generative AI is permitted, "always transparently cite its use"; if an AI platform "significantly influences your final product, consider informing people how you used AI"; AI-generated code "could be insecure or poorly built" and may carry IP risk. <https://uit.stanford.edu/security/responsibleai>
- **Office of Community Standards, Generative AI Policy Guidance** (adopted October 15, 2026) covers coursework only; it does not address staff work or software. <https://communitystandards.stanford.edu/generative-ai-policy-guidance>
- No OTL, Libraries or Provost guidance on attributing AI assistance in released code was found (see Unverified).

**Conclusion:** Stanford asks for transparency, not a specific form of words. Two practical implications for LabKit: (a) the code itself is Stanford-owned and was authored with a third-party AI tool, so the operations manager should confirm the Claude usage was under a Stanford-acceptable arrangement for Low Risk data (source code of an application that is about to be made public is, by definition, not proprietary going forward, but the question of what was entered during development is worth a sentence in the approval record); (b) the README and PROVENANCE disclosure already satisfy "transparently cite its use."

### 2.6 Export control, accessibility, data classification

- **Export control.** Publicly available software is generally outside EAR/ITAR, but Stanford's decision tree footnotes that public release of EAR-controlled encryption code is "generally authorized by License Exception TSU" provided the exporter gives the U.S. Government one-time notice of the code's location "prior to or at the time the code is placed in the public domain"; notice afterwards is a violation. Questions: exportcontrols@stanford.edu. Page created 01.27.21, changed 06.15.23. <https://doresearch.stanford.edu/export-controls-decision-tree-stanford-developed-software>; see also <https://doresearch.stanford.edu/resources/topics/export-controls-research-and-encryption>. LabKit's README mentions an AES-256 license-key component; if that is implemented by calling a standard library (CryptoKit, OpenSSL, Python `cryptography`) rather than implementing a cipher, the TSU notification burden is almost certainly nil, but a one-line email to exportcontrols@stanford.edu before release is cheap insurance.
- **Accessibility.** Administrative Guide 6.8.1, *Accessibility of Electronic Content*, last updated May 14, 2021, requires "websites; web- and mobile-based applications" of all Stanford units to meet WCAG 2.0 Level A and AA, with exceptions via the Office of Digital Accessibility. <https://adminguide.stanford.edu/chapters/computing/digital-accessibility/accessibility-electronic-content>. LabKit is a localhost web app used by Stanford staff; it falls within scope as an internally used application regardless of whether the code is public. Open-sourcing does not add an obligation, but the README should not claim conformance it has not tested.
- **GitHub service terms.** Cardinal Cloud GitHub is "approved for Low or Moderate Risk data only" and provides scanning for "embedded secrets, vulnerable code, and dependencies" (last modified June 24, 2026). <https://uit.stanford.edu/service/github>. Organization repositories are owned by the organization, not the individual; "Once you leave, your access may be revoked" (last modified December 5, 2024). <https://uit.stanford.edu/service/github/transfer>. The `sul-dlss` organization is the right home; a public repo may contain only Low Risk data.

---

## 3. sul-dlss convention (observed, 2026-11-01)

### 3.1 License distribution across the organization

GitHub API, `sul-dlss` public repositories (161 total, 158 not archived):

| GitHub-detected license | Count | Notes |
|---|---:|---|
| `NOASSERTION` ("Other") | 65 | In every case sampled this is **Apache-2.0 with a Stanford copyright line prepended**, which defeats GitHub's detector. |
| Apache-2.0 (detected) | 28 | Pristine Apache text; several leave the appendix placeholder unfilled. |
| No LICENSE file | 60 | Mostly recent infrastructure, FOLIO and prototype repos (e.g. `born-digital-processing`, `argo-b3`, `rialto-web`, `heracles-etd`, all 2025). |
| MIT | 4 | `voids` (2026), `sdr_view_components` (2025), others. |
| BSD-2-Clause | 1 | |

Source: `https://api.github.com/orgs/sul-dlss/repos?type=public` (pages 1–4). Apache-2.0 is therefore the convention for anything that carries a license (93 of 98 licensed repos). There is **no org-level `sul-dlss/.github` repository** (API returns 404), so there are no org-wide default LICENSE, CONTRIBUTING or PR templates.

### 3.2 Exact copyright wording found in LICENSE files

| Repository | First line of LICENSE | Form |
|---|---|---|
| argo | `© 2011 The Board of Trustees of the Leland Stanford Junior University.` | © + year + Board, then Apache boilerplate |
| dor-services-app | `© 2012 The Board of Trustees of the Leland Stanford Junior University.` | same |
| common-accessioning | `© 2011 The Board of Trustees of the Leland Stanford Junior University.` | same |
| exhibits | `© 2018 The Board of Trustees of the Leland Stanford Junior University.` | same |
| preservation_catalog | `© 2017 The Board of Trustees of the Leland Stanford Junior University.` | same |
| dlme | `© 2017 The Board of Trustees of the Leland Stanford Junior University.` | same |
| sul_pub | `Copyright 2015 The Board of Trustees of the Leland Stanford Junior University` | "Copyright" + year + Board |
| SearchWorks | `Copyright 2018 The Board of Trustees of the Leland Stanford Junior University.` | same |
| cocina-models, technical-metadata-service, sdr-api | Pristine Apache-2.0 text; no holder named | |
| happy-heron | Pristine Apache-2.0 text, appendix still reads `Copyright [yyyy] [name of copyright owner]` | unfilled template |
| **bdpl-labtools**, **bdpl-labtools-dedupe** | Pristine Apache-2.0 text, appendix line 190 still reads `Copyright [yyyy] [name of copyright owner]` | **unfilled template (to fix)** |

Fetched from `https://raw.githubusercontent.com/sul-dlss/<repo>/main/LICENSE`. The older, hand-made DLSS LICENSE files (argo family) are *short*: a one-line Stanford copyright notice followed by the 11-line Apache boilerplate from the license appendix, not the full 200-line license text. The newer ones are the full text with no holder.

### 3.3 READMEs, CONTRIBUTING, NOTICE, source headers

- **README attribution blocks:** none of argo, dor-services-app, cocina-models, happy-heron, exhibits, preservation_catalog, sul_pub or technical-metadata-service has a "built by," "Stanford Libraries" attribution, license or copyright section in its README (grep of `raw.githubusercontent.com/.../README.md`). READMEs are operational (badges, purpose, setup).
- **CONTRIBUTING.md, NOTICE, CODE_OF_CONDUCT.md, PR template:** absent (HTTP 404) in all eight repositories checked.
- **Source-file headers:** none. Sampled `argo/app/models/user.rb` and `cocina-models/lib/cocina/models.rb` begin with `# frozen_string_literal: true` and code; no copyright or license header.
- **sul-dlss-labs** (prototypes): a separate org, not surveyed in depth; its purpose is "Prototypes & Experiments." <https://github.com/sul-dlss-labs>

### 3.4 The BDPL repositories today

| Repo | Visibility | LICENSE | Copyright line | README attribution | AI disclosure |
|---|---|---|---|---|---|
| bdpl-labtools | public (created 2026-11-02 UTC) | Apache-2.0 full text | **unfilled** `[yyyy] [name of copyright owner]` | "Tools for the Born-Digital Preservation Lab (BDPL) at Stanford Libraries." License section only. | CONTRIBUTING.md speaks of "Everyone building here, human or AI"; 13 of recent 20 commits carry `Co-Authored-By: Claude …` |
| bdpl-labtools-dedupe | public (2026-11-02 UTC) | Apache-2.0 full text | **unfilled** | one-line purpose; License section | 5 of 5 commits carry the Claude trailer |
| bdpl-labtools-da-capture (LabKit) | **private** (created 2026-07-16) | **none** (`licenseInfo: null`) | n/a | README §"Provenance and authorship": "Created and directed by Michael Olson; implemented with Claude (Anthropic) under a mandatory branch → pull request → human-approval workflow" | 1,272 commits; 699 carry `Co-Authored-By: Claude <model>` trailers across five model versions (Fable 5: 326; Opus 5: 155; Fable 5.1: 121; Opus 4.8: 56; Opus 5.5: 41); `PROVENANCE.md` (last updated 2026-07-21 in its header, with a table current to 2026-08-01) records roles using PREMIS `eventRelatedAgentRole` terms (authorizer / implementer) |

Local inspection, 2026-11-01 (`/Users/mgolson/projects/da-capture-macos`, remote `sul-dlss/bdpl-labtools-da-capture`; `gh repo view`).

---

## 4. Attribution of AI assistance: how others word it

No Stanford wording exists, so the reference points are upstream open-source projects.

- **Linux kernel**, `Documentation/process/coding-assistants.rst` (merged December 23, 2025): "AI agents MUST NOT add Signed-off-by tags"; "Only humans can legally certify the Developer Certificate of Origin (DCO)"; the human submitter is responsible for reviewing AI-generated code, ensuring licensing compliance and "Taking full responsibility for the contribution." <https://www.kernel.org/doc/html/latest/process/coding-assistants.html>. The companion patch introduced the trailer form `Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]`, e.g. `Assisted-by: Claude:claude-3-opus coccinelle sparse`; an earlier `Co-developed-by` proposal was rejected because that tag implies a DCO-capable co-author. <https://lkml.iu.edu/hypermail/linux/kernel/2512.2/04871.html>; summary at <https://lilting.ch/en/articles/linux-kernel-ai-coding-assistant-policy>.
- **Fedora** (October 2025) and **NixOS** (2026) adopted declaration/trailer requirements for AI-assisted contributions, per <https://pasqualepillitteri.it/en/news/17291/linux-ai-2026-what-kernel-and-distros-decided> (secondary source; not independently verified here).
- **Scholarly-publishing norm (CASRAI):** "authorship entails accountability for the work, and a tool cannot be accountable," so AI is disclosed, not credited as author. <https://casrai.org/news/why-generative-ai-cannot-be-an-author-and-what-to-disclose>
- **GitHub's `Co-authored-by` trailer** is the mechanism LabKit already uses; GitHub renders it as a co-author avatar. It is widely used for AI pair-programming tools, but note the kernel's point: a `Co-authored-by` line for an AI implies a co-author who could hold copyright or certify origin, which it cannot. LabKit's `PROVENANCE.md` already addresses this directly ("Authorship is not agency"; the AI "never authorizes").

**Recommendation:** Keep the `Co-Authored-By: Claude <model> <noreply@anthropic.com>` trailers (changing 1,272 commits' history is neither possible without a rewrite nor desirable for a provenance-focused project). Going forward, consider switching the trailer to the kernel's `Assisted-by: Claude:<model-id>` form, which says what is meant without implying legal co-authorship; `PROVENANCE.md` should note the date of the change. In the README and LICENSE, name **only** the University as copyright holder and Michael Olson as the responsible human; describe Claude's role as implementation assistance.

---

## 5. Going-public checklist (recommendation)

| # | Step | Why / source | Status for LabKit |
|---|---|---|---|
| 1 | Written departmental approval from the operations manager, filed in the repo (e.g. `docs/release-approval.md`: date, approver, repo, license, copyright holder). | OTL Open Source Primer as quoted by Cramer 2015; RPH §3.B University ownership. | To do |
| 2 | Add LICENSE with filled copyright line; add NOTICE; fix the two public repos' unfilled appendix. | Apache-2.0 appendix: replace "the fields enclosed by brackets" <https://www.apache.org/licenses/LICENSE-2.0>; sul-dlss convention (§3.2). | To do (all three) |
| 3 | Full-history secret and PII scan (`gitleaks detect --source . --log-opts=--all`, `trufflehog git file://.`), plus a manual grep for SUNet IDs, email addresses, accession numbers, donor names, disk-image paths, and imaging logs. Rotate anything found; remember forks and caches persist. | GitHub: if the data is a secret, "you need to revoke and/or rotate that secret" first; data in forks "will continue to be accessible there." <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>. Cardinal Cloud GitHub is Low/Moderate risk only <https://uit.stanford.edu/service/github>. CONTRIBUTING.md already bans imaging outputs and accession-derived data. | To do; the existing CI `ci.yml` should gain a gitleaks job |
| 4 | Third-party license compatibility: confirm every runtime dependency in `DEPENDENCIES.md` (and `Brewfile`) is Apache-2.0-compatible (MIT, BSD, Apache, PSF, ISC, LGPL-dynamic are fine; GPL-only code *vendored into* the repo is not; GPL tools *invoked as separate processes* such as ClamAV are fine). Record the result in NOTICE or DEPENDENCIES.md. | Apache-2.0 §4(d) NOTICE attribution requirements <https://www.apache.org/licenses/LICENSE-2.0>; ASF guidance that third-party notices belong in NOTICE and must not be altered <https://www.apache.org/legal/src-headers.html>. | To do |
| 5 | Export control: email exportcontrols@stanford.edu describing the AES-256 license-key component (library used, no custom cryptography) and ask whether TSU notification applies. Keep the reply. | Stanford decision tree, 06.15.23 <https://doresearch.stanford.edu/export-controls-decision-tree-stanford-developed-software> | To do (likely "no action") |
| 6 | Names and marks: no Stanford logo/seal in repo or UI; product name stays "BDPL LabKit"; README says "built at Stanford Libraries," not "a Stanford product." | Admin Guide 1.5.4 (2017-07-25); Name Use Guidelines (amended Oct 2025). | Review `macos/` UI assets |
| 7 | Accessibility: state honestly in README what has been tested against WCAG 2.0/2.1 AA; do not claim conformance. | Admin Guide 6.8.1 (2021-05-14). | Documentation only |
| 8 | AI-use record: one paragraph in the approval memo confirming the AI tooling used was acceptable for the data risk level of what was entered (code, lab procedures; no collection content or High Risk data). | UIT Responsible AI <https://uit.stanford.edu/security/responsibleai>. | To do |
| 9 | Register in the OpenSource@Stanford Projects Registry (optional) and, if wanted, request a licensing consult. | <https://opensource.stanford.edu/> | Optional |
| 10 | Flip visibility; enable Dependabot/secret scanning/push protection on the public repo; add `SECURITY.md` (bdpl-labtools already has one). | Cardinal Cloud GitHub scanning features. | After 1–8 |

**Not required:** OTL invention disclosure (unpatentable workflow software; RPH Copyright Policy §1.A/§2.G route is disclosure *if* Stanford wants to assert ownership, which it already has by work-for-hire); Trademark Licensing review (unit-level use); a formal Stanford "release record" (none exists).

---

## 6. Templates (recommendation)

### 6.1 LICENSE

Use the **full Apache-2.0 text** (as cocina-models, bdpl-labtools do) and fill in the appendix. Alternatively follow the older DLSS short form (argo, exhibits) of a copyright line plus the 11-line boilerplate; both are valid, but the full text is what GitHub detects and what OSI recommends. Replace line 190 of the current `bdpl-labtools` and `bdpl-labtools-dedupe` LICENSE files, and add to LabKit, exactly:

```
   Copyright 2026 The Board of Trustees of the Leland Stanford Junior University

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

For LabKit, whose first commit dates from 2026-07-16, use `Copyright 2026`. Use a range (`2026-2027`) only once work continues into another year. The sul-dlss repos use a single origin year and never update it; that is acceptable.

### 6.2 NOTICE

sul-dlss does **not** use NOTICE files (none in the eight repos checked). Apache-2.0 does not require one for your own code; it requires that if a NOTICE exists, downstream redistributors preserve it (§4(d)). A short NOTICE is nevertheless recommended for LabKit because it bundles or depends on third-party components whose own notices must travel with it, and because it is the conventional home for the attribution you want preserved in forks (ASF: copyright notices go in NOTICE, not in source headers <https://www.apache.org/legal/src-headers.html>).

```
BDPL LabKit
Copyright 2026 The Board of Trustees of the Leland Stanford Junior University

This product was developed at Stanford University Libraries, Born-Digital
Preservation Lab (BDPL), by Michael Olson, with implementation assistance
from Claude (Anthropic) under human review of every change. See
PROVENANCE.md for the full statement of responsibility.

This product includes software developed by third parties. Their licenses
and notices are listed in DEPENDENCIES.md.
```

### 6.3 README "Attribution" section

Place after the project description and before installation. Mirror in bdpl-labtools and bdpl-labtools-dedupe with the second paragraph adjusted.

```markdown
## Attribution

BDPL LabKit is built and maintained by the Born-Digital Preservation Lab
(BDPL) at [Stanford University Libraries](https://library.stanford.edu/).
Copyright © 2026 The Board of Trustees of the Leland Stanford Junior
University. Released under the [Apache License 2.0](LICENSE).

**Design lead and responsible author:** Michael Olson, Stanford Libraries.
Every requirement, design decision and merged change was set, reviewed and
approved by him.

**AI-assisted development.** The code, tests and documentation were written
with Claude (Anthropic) acting as implementing developer under direction.
Each commit names the model version that assisted it in a
`Co-Authored-By: Claude …` trailer; the roles of human and AI, the models
used, and the dating evidence are recorded in [PROVENANCE.md](PROVENANCE.md).
AI assistance is disclosed as a matter of provenance; it does not confer
authorship or copyright, which rest with the University and its staff.

This project is not an official Stanford University product and its
release does not imply University endorsement. "Stanford" and the Stanford
marks are trademarks of the Board of Trustees of the Leland Stanford Junior
University and are used here only to identify the originating unit.
```

### 6.4 Source-file header

sul-dlss does not use per-file headers (§3.3), and ASF practice is to keep copyright notices out of source files. **Recommendation: do not add headers.** If a one-liner is wanted for files likely to be copied out of context (for example a standalone script), use the SPDX form, which is machine-readable and short:

```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 The Board of Trustees of the Leland Stanford Junior University
```

### 6.5 Commit trailer going forward

Keep the existing trailers. Optionally adopt the kernel form in new commits and note the switch date in PROVENANCE.md:

```
Assisted-by: Claude:claude-fable-5-1
```

### 6.6 Release-approval record (`docs/release-approval.md`)

```
Repository: sul-dlss/bdpl-labtools-da-capture
Decision: approved for public release under Apache-2.0
Copyright holder: The Board of Trustees of the Leland Stanford Junior University
Basis: RPH Copyright Policy §3.B (work-for-hire by staff); OTL Open Source
Primer (departmental approval suffices for staff-developed software)
Approved by: <name, title>, Stanford Libraries, <date>
Checks completed: secret/PII history scan (<tool, date>); dependency
license review (DEPENDENCIES.md, <date>); export-control query to
exportcontrols@stanford.edu (<date, answer>); AI-tool data-risk review.
```

---

## 7. Comparison with other institutions (brief)

- **Harvard Library** reportedly directs that "wherever possible, code developed as open source by Harvard Library or Harvard Library Technology Services be released with the Apache 2.0 license" (search snippet from the Harvard wiki; the page itself could not be fetched, see Unverified).
- **University of California** asks that University-owned software bear the notice "This software is Copyright © 2XXX The Regents of the University of California." <https://innovation.ucsd.edu/disclose-patent/copyright.html>. Same structure as Stanford's "Board of Trustees" line.
- **UC Berkeley OTL** requires a software disclosure form naming the intended open-source license, signed by all authors, before release. <https://ipira.berkeley.edu/faq/general/i-have-developed-some-software-and-would-release-it-under-open-source-software-license>. Stanford has no equivalent form for unpatentable software.
- **UNT Libraries** encourages contribution to OSI-licensed projects and supplies a BSD-3-Clause template for in-house code. <https://library.unt.edu/policies/open-source-software/>
- **Samvera (Hydra) community**, of which DLSS was a founding member, standardized Apache 2 with a LICENSE.txt header beginning with the originating institution and year (the canonical example lists "Stanford University (2012)") and the sentence "Additional copyright may be held by others, as reflected in the commit history." <https://samvera.atlassian.net/wiki/x/DAonG> (via search summary; the wiki's IP pages were marked archived in 2022). This explains the argo-style LICENSE files and is a sensible optional second line for LabKit if outside contributors ever join.

---

## 8. Unverified / gaps

- **OTL Open Source Primer.** Known only through Tom Cramer's 2015 CODE4LIB quotation. No live or archived copy was found on otl.stanford.edu in 2026; the "departmental approval" rule should be confirmed with OTL (otl-information@stanford.edu) or OpenSource@Stanford before it is cited in the approval memo as current policy.
- **Harvard Library open source policy page** (harvardwiki.atlassian.net) returned "Page Not Found"; the Apache-2.0 preference is from a search snippet only.
- **Samvera Code Copyright Statement** page could not be fetched directly; wording is from search-result summaries.
- **Fedora/NixOS AI-declaration rules** are from one secondary article and were not checked against primary sources.
- **Whether DLSS has an internal (intranet/Confluence) open-source or licensing guideline** could not be determined from public sources; the design lead should ask DLSS management. Observed GitHub practice is the only evidence.
- **Stanford Libraries-specific or Provost-level guidance on AI attribution in staff work** was not found; the UIT page is the only Stanford statement located.
- **WCAG 2.1 expectation for applications revised after April 1, 2022** appears on a secondary Stanford site, not in Admin Guide 6.8.1 itself, which still says WCAG 2.0.
- **The exact cryptographic implementation** of LabKit's license-key component was not inspected for this report; the export-control recommendation assumes standard-library use.
- GitHub repository creation timestamps for bdpl-labtools and bdpl-labtools-dedupe read 2026-11-02 UTC (the evening of 2026-11-01 Pacific).

---

## Sources

Stanford policy and offices

- Research Policy Handbook, Copyright Policy (v. 2018-03-18): <https://doresearch.stanford.edu/policies/research-policy-handbook/intellectual-property/copyright-policy>
- Research Policy Handbook, Inventions, Patents and Licensing (v. 2023-10-30): <https://doresearch.stanford.edu/policies/research-policy-handbook/intellectual-property/inventions-patents-and-licensing>
- Archived 1998 RPH 5.2 Copyright Policy (for history): <https://webarchive.library.unt.edu/eot2008/20090116013126/http://www.stanford.edu/dept/DoR/rph/5-2.html>
- OTL, Software: <https://otl.stanford.edu/software>
- OTL webinar deck listing otl-information@stanford.edu (2020-11-09): <https://med.stanford.edu/content/dam/sm/mchri/documents/about/Stanford%20MCHRI%20Webinar_OTL_Non-Confidential_11092020.pdf>
- OpenSource@Stanford: <https://opensource.stanford.edu/>; Sloan grant: <https://sloan.org/grant-detail/g-2025-25270>
- SUETRI-B software page (OTL "prescribed" OSS terms): <https://suetri-b.stanford.edu/affiliates/affiliate-resources/software>
- Administrative Guide 1.5.4, Trademarks (2017-07-25): <https://adminguide.stanford.edu/chapters/guiding-policies-and-principles/conflict-interest/ownership-and-use-stanford-trademarks>
- Name Use Guidelines (2014-03-01, amended Oct 2025): <https://trademarks.stanford.edu/name-use-guidelines>
- InVEST trademark policy: <https://naturalcapitalproject.stanford.edu/software/invest/invest-trademark-and-logo-use-policy>
- UIT, Responsible AI: <https://uit.stanford.edu/security/responsibleai>
- Office of Community Standards, Generative AI Policy Guidance (2026-10-15): <https://communitystandards.stanford.edu/generative-ai-policy-guidance>
- Export Controls Decision Tree: Stanford-Developed Software (2023-06-15): <https://doresearch.stanford.edu/export-controls-decision-tree-stanford-developed-software>; Research and Encryption: <https://doresearch.stanford.edu/resources/topics/export-controls-research-and-encryption>
- Administrative Guide 6.8.1, Accessibility of Electronic Content (2021-05-14): <https://adminguide.stanford.edu/chapters/computing/digital-accessibility/accessibility-electronic-content>
- UIT, Cardinal Cloud GitHub (2026-06-24): <https://uit.stanford.edu/service/github>; repository transfer/departure (2024-12-05): <https://uit.stanford.edu/service/github/transfer>

sul-dlss practice

- Tom Cramer, CODE4LIB, 2015-01-10: <https://www.mail-archive.com/code4lib@listserv.nd.edu/msg26366.html>
- GitHub org: <https://github.com/sul-dlss>; API: <https://api.github.com/orgs/sul-dlss/repos?type=public>
- LICENSE files: <https://raw.githubusercontent.com/sul-dlss/argo/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/dor-services-app/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/exhibits/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/preservation_catalog/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/sul_pub/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/SearchWorks/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/common-accessioning/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/dlme/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/cocina-models/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/happy-heron/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/technical-metadata-service/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/sdr-api/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/bdpl-labtools/main/LICENSE>, <https://raw.githubusercontent.com/sul-dlss/bdpl-labtools-dedupe/main/LICENSE>
- Samvera Code Copyright Statement: <https://samvera.atlassian.net/wiki/x/DAonG>

Licensing references

- Apache License 2.0 text and appendix: <https://www.apache.org/licenses/LICENSE-2.0>
- ASF source headers and NOTICE policy: <https://www.apache.org/legal/src-headers.html>
- GitHub, Removing sensitive data from a repository: <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>

AI attribution norms

- Linux kernel, Coding Assistants: <https://www.kernel.org/doc/html/latest/process/coding-assistants.html>; patch v2 with `Assisted-by:` format: <https://lkml.iu.edu/hypermail/linux/kernel/2512.2/04871.html>; summary: <https://lilting.ch/en/articles/linux-kernel-ai-coding-assistant-policy>; distro overview (secondary): <https://pasqualepillitteri.it/en/news/17291/linux-ai-2026-what-kernel-and-distros-decided>
- CASRAI, why generative AI cannot be an author: <https://casrai.org/news/why-generative-ai-cannot-be-an-author-and-what-to-disclose>

Other institutions

- UC San Diego / UC copyright notice: <https://innovation.ucsd.edu/disclose-patent/copyright.html>
- UC Berkeley OTL open-source FAQ: <https://ipira.berkeley.edu/faq/general/i-have-developed-some-software-and-would-release-it-under-open-source-software-license>
- UNT Libraries open source policy: <https://library.unt.edu/policies/open-source-software/>
- Harvard Library (search snippet only): <https://harvardwiki.atlassian.net/wiki/x/1KWUAg>
