# Flask Project for Product Tag Creation

## Description
This project implements a Flask API for creating product tags, using dynamically generated Code128 barcodes based on a provided product code.

## Setup and Execution
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Run the Flask server using `python run.py`

## Example API Usage
The API can be accessed at http://localhost:5000/create_tag with a POST method, sending a JSON with the following format:
```{
    "product_code": "ABCDE12345"
}
```

## Contact
Developed by Gabriela Alvarenga.
For any questions or feedback, please contact me at [email](mailto:gabrielasalvarenga2@gmail.com) or visit my [LinkedIn](https://www.linkedin.com/in/gabrieladsalvarenga/) or reach me at [github](https://www.github.com/gabrieladsalv).
