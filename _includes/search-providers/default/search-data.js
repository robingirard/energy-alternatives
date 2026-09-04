{%- comment -%}
Index de recherche cote client.

Le fichier /assets/search.js est unique pour tout le site : on y publie donc un
index par langue, et le script choisit celui qui correspond a l'attribut `lang`
de la page consultee. Depuis /en/... la recherche ne renvoie que des articles
anglais, et inversement.
{%- endcomment -%}
{%- assign _search_documents = site.posts | concat: site.posts_en | sort: 'date' | reverse -%}
window.TEXT_SEARCH_DATA_BY_LANG={
{%- for _search_language in site.languages -%}
  {%- unless forloop.first -%},{%- endunless -%}
  {%- assign _search_locale = site.data.locale[_search_language.code] | default: site.data.locale.en -%}
  {%- assign _search_group = _search_locale.SEARCH_GROUP_POSTS | default: 'Posts' -%}
  {{ _search_language.code | jsonify }}:{
    {{ _search_group | jsonify }}:[
      {%- assign _search_is_first = true -%}
      {%- for _article in _search_documents -%}
        {%- assign _article_lang = _article.lang | default: site.lang | slice: 0, 2 -%}
        {%- if _article_lang == _search_language.code -%}
          {%- unless _search_is_first -%},{%- endunless -%}
          {%- assign _search_is_first = false -%}
          {%- include snippets/prepend-baseurl.html path=_article.url -%}
          {"title":{{ _article.title | jsonify }},"url":{{ __return | jsonify }}}
        {%- endif -%}
      {%- endfor -%}
    ]
  }
{%- endfor -%}
};
window.TEXT_SEARCH_DATA=(function(data){
  var lang=(document.documentElement.lang||'').slice(0,2);
  return data[lang]||data[{{ site.lang | slice: 0, 2 | jsonify }}]||{};
})(window.TEXT_SEARCH_DATA_BY_LANG);
