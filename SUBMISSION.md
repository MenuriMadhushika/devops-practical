# DevOps Practical Submission

**Student name:** HGTM Madhushika  
**Student ID:** 36833  
**GitHub repository:** https://github.com/menurimadhushika/devops-practical  
**Docker Hub image:** [Add Docker Hub image URL]  
**Render service:** [Add live Render URL]

## Project summary

This project packages a Flask web application and its automated test, runs the test on every push to `main` with GitHub Actions, builds a Docker image, and declares a two-replica Kubernetes deployment with a NodePort service. The application reads the `PORT` environment variable for cloud hosting and defaults to port 5000 locally. The V2 response is `CI/CD and Docker Pipeline is a massive success! V2`.

## Repository contents

- `app.py` — Flask application and configurable port.
- `test_app.py` — HTTP response and status test.
- `requirements.txt` — Python dependencies.
- `.github/workflows/ci.yml` — push-triggered automated test workflow.
- `Dockerfile` — container build and Gunicorn startup.
- `k8s/deployment.yaml` — two desired replicas.
- `k8s/service.yaml` — NodePort service forwarding to port 5000.

## Implementation and verification

### 1. Version control and application

The repository is initialized with Git. The Flask route returns the V2 success message. The automated test checks for HTTP 200 and the expected response body.

**Evidence to insert:** screenshot of repository files and successful test output (`pytest -q`).

### 2. Continuous integration

The GitHub Actions workflow runs on pushes to `main`, checks out the repository, installs dependencies, and runs PyTest. A green workflow run confirms the quality gate passed.

**Evidence to insert:** screenshot of the successful GitHub Actions run.

### 3. Containerization

The Docker image installs the declared dependencies and starts the Flask WSGI application with Gunicorn. The image is intended to be published as `YOUR_DOCKERHUB_USERNAME/flask-app:v1`.

**Evidence to insert:** successful `docker build` output, local HTTP response, and public Docker Hub image page.

### 4. Kubernetes deployment and resilience

The deployment declares two replicas labeled `app: flask-web`; the service selects those pods and maps port 80 to container port 5000. Kubernetes maintains the desired replica count. To demonstrate self-healing, record the pod list, delete one pod, and show that a replacement reaches Running while two replicas remain available.

**Evidence to insert:** `kubectl get pods` showing two Running replicas before and after deleting one pod, plus the service URL response.

### 5. Continuous deployment

The Render web service is connected to the public GitHub repository and configured to build with the Dockerfile from `main`. The application listens on Render's `PORT`. After the service first becomes Live, the V2 change is pushed to GitHub; the live URL should then serve the updated response.

**Evidence to insert:** Render Live page and browser/curl result showing the V2 response after the final push.

## Submission checklist

- [ ] Replace the student details and all account placeholders.
- [ ] Publish the project to a public GitHub repository named `devops-practical`.
- [ ] Publish the Docker image and update `k8s/deployment.yaml` with the real image name.
- [ ] Run the Kubernetes deployment and capture the self-healing demonstration.
- [ ] Configure Render from the GitHub repository and verify the live V2 response.
- [ ] Add the requested screenshots/evidence to this report before submitting.

## Conclusion

The repository contains the source, test, CI workflow, container definition, and Kubernetes manifests needed for the practical. The final assessment evidence must be captured from the student's own GitHub, Docker Hub, Kubernetes, and Render accounts after running the deployment steps.



