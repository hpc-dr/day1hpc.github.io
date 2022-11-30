require "open-uri"
require "nokogiri"
require "json"

def parse_article_info(doc)
  result = []
  # get the articles
  doc.css("article").each do |article|
    a = {
      title: article.css(".blog-post-title a span")[0].text,
      url: article.css(".blog-post-title a")[0].attribute("href"),
      datePublished: article.css("footer time[property=datePublished]").text,
      image: nil,
      categories: [],
      excerpt: article.css("section.blog-post-excerpt").text.strip,
    }
    # fill out the categories
    article.css("footer span.blog-post-categories a").each do |c|
      if c.text then a[:categories].push(c.text) end
    end
    # image sometimes missing 
    if article.css("meta[property=image]").length > 0 then
      a[:image] =  article.css("meta[property=image]").attribute("content").value 
    end
    result.append(a)
  end
  return result
end

page = "https://aws.amazon.com/blogs/aws/"
results = []
while true
  @doc = Nokogiri::Slop(URI.open(page))
  # parse the article info out
  results += parse_article_info(@doc)
  #see if there is a next page
  nxt = @doc.css("head link[rel='next']")
  if nxt.length > 0
    page = nxt[0].attribute('href').value
  else
    break
  end
end
f = open('./news-blog-posts.json','w') 
f.write(results.to_json)
