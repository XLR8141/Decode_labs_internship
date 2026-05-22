import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

class DataClassificationEngine:
    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.scaler = StandardScaler()

    def prepare_data(self):
        dataset = load_iris()
        x_raw = dataset.data
        y = dataset.target
        
        x_scaled = self.scaler.fit_transform(x_raw)
        
        return train_test_split(
            x_scaled, y, test_size=0.2, random_state=42, stratify=y
        )

    def train_and_evaluate(self):
        x_train, x_test, y_train, y_test = self.prepare_data()
        
        self.model.fit(x_train, y_train)
        
        predictions = self.model.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)
        
        print("Project 2: Data Classification Results")
        print(f"Validation Accuracy: {accuracy * 100:.2f}%")
        print("Classification Report:")
        print(classification_report(y_test, predictions))

if __name__ == "__main__":
    engine = DataClassificationEngine()
    engine.train_and_evaluate()