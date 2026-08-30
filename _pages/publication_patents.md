---
layout: page
permalink: /publications/patents/
title: Publications
description: Patents
nav: false
publication_section: patents
---

{% include publications_switcher.liquid %}

{% include bib_search.liquid %}

<div class="publications">
  <h2 class="bibliography">Registered Patents</h2>
  <ol class="bibliography">
    {% for patent in site.data.patents.registered %}
      <li>{% include patent_entry.liquid patent=patent status="Registered" %}</li>
    {% endfor %}
  </ol>

  <h2 class="bibliography">Patent Applications</h2>
  <ol class="bibliography">
    {% for patent in site.data.patents.applications %}
      <li>{% include patent_entry.liquid patent=patent status="Application" %}</li>
    {% endfor %}
  </ol>
</div>
