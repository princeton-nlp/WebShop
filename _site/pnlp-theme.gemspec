Gem::Specification.new do |s|
  s.name          = "pnlp-theme"
  s.version       = "1.0.0"
  s.license       = "CC0-1.0"
  s.authors       = ["John Yang", "Princeton University"]
  s.email         = ["jy1682@princeton.edu"]
  s.homepage      = "https://github.com/princeton-nlp/project-page-template"
  s.summary       = "Princeton NLP Project Landing Page Template"

  s.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^((_includes|_layouts|_sass|assets)/|(LICENSE|README)((\.(txt|md|markdown)|$)))}i)
  end

  s.required_ruby_version = ">= 2.4.0"

  s.platform = Gem::Platform::RUBY
  s.add_runtime_dependency "jekyll", "> 3.5", "< 5.0"
  s.add_runtime_dependency "jekyll-seo-tag", "~> 2.0"
end