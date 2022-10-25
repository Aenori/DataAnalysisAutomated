# DataAnalysisAutomated

After installing the required modules :

    pip install -r requirements.txt

You can run the application with :

    python main.py

If you have docker installed, you can run it :

    docker build . -t python_reporting
    docker run -v $(pwd):/app python_reporting

The part that say $(pwd) might have to be adapted in windows to point to the local directory.
