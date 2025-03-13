require "open-uri"
require "nokogiri"
require "json"
require "uri"

def parse_article_info(doc)
  result = []
  doc.css("article").each do |article|
    a = {
      title: article.at_css(".blog-post-title a span")&.text,
      url: article.at_css(".blog-post-title a")&.[]("href"),
      datePublished: article.at_css("footer time[property='datePublished']")&.text,
      image: article.at_css("meta[property='image']")&.[]("content"),
      categories: article.css("footer span.blog-post-categories a").map(&:text),
      excerpt: article.at_css("section.blog-post-excerpt")&.text&.strip,
    }
    result << a
  end
  result
end

base_url = "https://aws.amazon.com"
page = "#{base_url}/blogs/quantum-computing/"
results = []

loop do
  puts "Fetching: #{page}"

  begin
    html = URI.open(page,
                    "User-Agent" => "Mozilla/5.0",
                    "Accept" => "text/html",
                    "Referer" => base_url).read
  rescue OpenURI::HTTPError => e
    puts "HTTP error fetching #{page}: #{e.message}"
    break
  end

  doc = Nokogiri::Slop(html)
  results += parse_article_info(doc)

  # Find the rel=next link and resolve full URL
  next_link = doc.at_css("head link[rel='next']")
  break unless next_link

  next_href = next_link["href"]
  break unless next_href && !next_href.empty?

  # Resolve relative → absolute URL
  page = URI.join(base_url, next_href).to_s
end

# Write to JSON file
File.open('./quantum-computing-blog-posts.json', 'w') do |f|
  f.write(JSON.pretty_generate(results))
end

puts "Done. Parsed #{results.size} articles."
