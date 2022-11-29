require "json"
require "csv"

abort("ERROR: Need an input JSON file") unless ARGV.length > 0

i = open(ARGV[0])
o = ARGV[0].sub(".json", ".csv")

'''
{
  "title": "Getting the Best Price Performance for Numerical Weather Prediction Workloads on AWS",
  "url": "https://aws.amazon.com/blogs/hpc/best-price-performance-for-nwp-on-aws/",
  "datePublished": "27 SEP 2022",
  "image": "https://d2908q01vomqb2.cloudfront.net/e6c3dd630428fd54834172b8fd2735fed9416da4/2022/09/19/hpcblog-131-featured-img.png",
  "categories": [
    "Best Practices",
    "High Performance Computing"
  ],
  "excerpt": "In this post, we will provide an overview of Numerical Weather Prediction (NWP) workloads, and the AWS HPC-optimized services for it. We’ll test three popular NWP codes: WRF, MPAS, and FV3GFS."
},
'''

headers = %w[
  title
  URL
  image
  datePublished
  categories
  excerpt
]


articles = JSON.parse(i.read())
CSV.open(o,'wb') do |csv|
  csv << headers
  articles.each do |a| 
    csv << [
      a["title"], 
      a["url"],
      a["image"],
      a["datePublished"],
      a["categories"] ? a["categories"].join(" | ") : "",
      a["excerpt"]
    ]
  end
end


