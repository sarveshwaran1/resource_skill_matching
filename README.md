**Resource Skill Matching**

This is a Django based API for matching resources to tasks based on their skills and availability. It includes postman collection to create and view the projects, tasks, skills, resources, their relationships and to find matching resources for a given task.

**Installation Steps:**

1. **Clone the repository**:
   ```bash
    git clone https://github.com/sarveshwaran1/resource_skill_matching.git
    cd resource-matching-api
    ```
2.  **Create and activate a virtual environment**:

    ```bash
    python -m venv myenv
    ```
3.  **Install the requirements**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create and apply migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the server**:

    ```bash
    python manage.py runserver
    ```

**Note**: I have added the sequence and ER diagranm in the **Diagram** folder.
