# Lexical Analyzer in Ruby
# Language: Ruby
# Developed by: Anar, Dan, Gary

class Lexer
    # Define token categories using regex and lists
    KEYWORDS = %w[int if else return]
    OPERATORS = %w[+ - * / = >= <= != == > <]
    SEPARATORS = %w[{ } ( ) ; ,]

    def initialize(file_path)
        @file_path = file_path
        @tokens = []  # Store final tokens as [lexeme, token_type]
    end

    # Read file and lexically analyze
    def analyze
        content = File.read(@file_path)
        content = remove_comments(content)
        tokenize(content)
        display_tokens
    end

    # Remove comments
    def remove_comments(code)
        code.gsub!(/\/\/.*$/, "")        # Single-line comments
        code.gsub!(/\/\*.*?\*\//m, "")  # Multi-line comments
        code
    end

    # Tokenize code
    def tokenize(code)
        # Regex pattern to identify lexemes
        pattern = /\b[a-zA-Z_][a-zA-Z0-9_]*\b|[0-9]+|\S/ 
        code.scan(pattern).each do |lexeme|
            classify_token(lexeme.strip) unless lexeme.strip.empty?
        end
    end

    # Classify lexemes into token categories
    def classify_token(lexeme)
        if KEYWORDS.include?(lexeme)
            @tokens << [lexeme, "KEYWORD"]
        elsif OPERATORS.include?(lexeme)
            @tokens << [lexeme, "OPERATOR"]
        elsif SEPARATORS.include?(lexeme)
            @tokens << [lexeme, "SEPARATOR"]
        elsif lexeme.match(/^\d+$/)
            @tokens << [lexeme, "INTEGER"]
        elsif lexeme.match(/^".*"$/)
            @tokens << [lexeme, "STRING_LITERAL"]
        else
            @tokens << [lexeme, "IDENTIFIER"]
        end
    end

    # Display tokens in required format
    def display_tokens
        @tokens.each do |lexeme, token_type|
            puts "\"#{lexeme}\" = #{token_type.downcase}"
        end
    end
end

# Example usage
if ARGV.empty?
    puts "Usage: ruby lexer.rb <file_path>"
    exit
end

lexer = Lexer.new(ARGV[0])
lexer.analyze