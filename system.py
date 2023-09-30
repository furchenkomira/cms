class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class CMS:
    def __init__(self):
        self.articles = []

    def create_article(self, title, content):
        article = Article(title, content)
        self.articles.append(article)
        print("Article created successfully.")

    def view_articles(self):
        if not self.articles:
            print("No articles found.")
        else:
            print("Articles:")
            for index, article in enumerate(self.articles, start=1):
                print(f"{index}. Title: {article.title}")
                print(article.content)
                print()

    def update_article(self, index, title, content):
        if 0 <= index < len(self.articles):
            article = self.articles[index]
            article.title = title
            article.content = content
            print("Article updated successfully.")
        else:
            print("Invalid article index.")

    def delete_article(self, index):
        if 0 <= index < len(self.articles):
            deleted_article = self.articles.pop(index)
            print(f"Deleted article: {deleted_article.title}")
        else:
            print("Invalid article index.")

def main():
    cms = CMS()

    while True:
        print("\nContent Management System Menu:")
        print("1. Create Article")
        print("2. View Articles")
        print("3. Update Article")
        print("4. Delete Article")
        print
