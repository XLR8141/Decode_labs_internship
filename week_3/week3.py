import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.items = [
            {"title": "Python for Data Science", "tags": "python data science programming machine learning"},
            {"title": "Web Development Bootcamp", "tags": "html css javascript web design frontend"},
            {"title": "Advanced Machine Learning", "tags": "ai machine learning python statistics math"},
            {"title": "Digital Marketing 101", "tags": "marketing seo social media advertising"},
            {"title": "Automation with n8n", "tags": "automation workflow python tools productivity"}
        ]

    def get_recommendations(self, user_interests):
        item_tags = [item["tags"] for item in self.items]
        
        all_texts = [user_interests] + item_tags
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)
        
        user_vector = tfidf_matrix[0]
        item_vectors = tfidf_matrix[1:]
        
        similarity_scores = cosine_similarity(user_vector, item_vectors).flatten()
        
        results = []
        for i in range(len(self.items)):
            results.append((self.items[i]["title"], similarity_scores[i]))
            
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def run(self):
        print("DecodeLabs Personalization Phase")
        user_input = input("Enter your technical interests: ")
        
        recommendations = self.get_recommendations(user_input)
        
        print("Recommended for you:")
        for title, score in recommendations:
            if score > 0:
                print(f"Match: {title} (Score: {score:.2f})")

if __name__ == "__main__":
    engine = RecommendationEngine()
    engine.run()