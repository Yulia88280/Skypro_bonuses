import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "X-API-Key": api_key
        }
    
    def purchase (self, product_id, student_id, added_by):
        url = f"{self.base_url}/bonuses/purchases"
        payloud = {
            "product_id": product_id,
            "student_id": student_id,
            "added_by": added_by
        }
        response = requests.post(url, json=payloud, headers=self.headers)
        return response
    def get_purchase(self):
        url = f"{self.base_url}/bonuses/purchases"
        response = requests.get(url, headers=self.headers)
        return response
    