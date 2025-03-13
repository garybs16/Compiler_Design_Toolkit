# Lexical analyzer
# Langauge: Ruby
# Developed by: Anar Otgonbaatar, Gary, Dan

class Lexer
	# Define token categories using regex and lists
	KEYWORDS = 
	OPERATORS = 
	SEPARATORS = 

	def intialize( file_path )
		@file_path = file_path
		@tokens = []	# Store final tokens as [lexeme, token_type]
	end

	# Read file and lexically analyze
	def analyze
		content = File.read( @file_path )
		content = remove_comments( content )
		tokenize( content )
		display_tokens
	end

	# Remove comments
	def remove_comments( code )
		code.gsub!(/\/\/.*/, "")	# Single line comments
		code.gsub!(/\/\*.*?\*\//m, "")	# Multi line comments
		code
	end

	# Tokenize
	def tokenize( code )
		# Regex patterns to id lexemes
		pattern = /
		/x

		code.scan( pattern ).each do |lexeme|
			classify_token( lexeme.strip ) unless lexeme.strip.empty?
		end
	end

	# Classify lexemes into token categories
	def classify_token( lexeme )

	end

	# Display tokens
	def display_tokens
		@tokens.each.do |lexeme, token_type|
			puts "\"#{lexeme}\" = #{token_type.downcase}"
		end
	end
