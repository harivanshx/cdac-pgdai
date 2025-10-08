from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello Harivansh</title>
  <style>
 
    body {
      font-family: Inter, Roboto, system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      margin: 0;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .card {
      background: #ffffff;
      padding: 2rem 3rem;
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12);
      text-align: center;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(15, 23, 42, 0.14);
    }

    h1 {
      margin: 0;
      font-size: 2.4rem;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    p {
      margin-top: 0.5rem;
      color: #475569;
    }

    @media (max-width: 480px) {
      .card { padding: 1.4rem 1.6rem; }
      h1 { font-size: 1.6rem; }
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello Everyone </h1>
    <p>Welcome to my Flask Application</p>
    <p> made with love by Harivansh Bhardwaj</p>
  </div>
</body>
</html>
'''


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
