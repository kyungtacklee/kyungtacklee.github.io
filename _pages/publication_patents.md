---
layout: page
permalink: /publications/patents/
title: Publications
description: Patents and patent applications
nav: false
publication_section: patents
---

{% include publications_switcher.liquid %}

This page lists registered patents and active pending applications. Standalone applications recorded as abandoned or on hold are not listed as pending; jurisdiction-specific status is noted within a registered record where relevant.

{% include bib_search.liquid %}

<div class="publications">
  <h2 class="bibliography">Registered Patents</h2>
  <ol class="bibliography">
    {% for patent in site.data.patents.registered %}
      <li>{% include patent_entry.liquid patent=patent status="Registered" %}</li>
    {% endfor %}
  </ol>

  <h2 class="bibliography">Pending Applications</h2>
  <ol class="bibliography">
    {% for patent in site.data.patents.pending %}
      <li>{% include patent_entry.liquid patent=patent status="Pending" %}</li>
    {% endfor %}
  </ol>
</div>
