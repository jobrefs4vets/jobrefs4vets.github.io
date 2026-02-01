---
layout: jobs
title: Job Listings
---

# Job Listings

{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign active_jobs = site.jobs | where_exp: "job", "job.validThrough >= today" %}

<ul>
{% for job in active_jobs %}
  <li>
    <a href="{{ job.url }}">{{ job.title }}</a>
    — {{ job.jobLocation.city }}, {{ job.jobLocation.region }}
  </li>
{% endfor %}
</ul>