require 'nokogiri'
require 'open-uri'

url = Nokogiri::HTML(open('http://localhost:5000/'))

url.css('h1').each do |title| 
    puts title.content
end
