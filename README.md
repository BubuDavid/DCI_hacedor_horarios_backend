![DCI Logo](https://i.imgur.com/BWjEV8J.png)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


# API - Hacedor de Horarios
- *Project made with FastAPI*
- The frontend can be found in [this repo](https://github.com/BubuDavid/DCI_hacedor_horarios_frontend)

# How is it conformed?
- 🗃️ Data Part:
	- ⛏️ Web Scraping
	- 🐼 Data Transformation
	- 🧹 Data Cleansing
	- 📤 Export the data
- ⌨️ Algorithm:
	- ...
- 🍕 API with FastAPI

# DCI Scholar Scheduler


DCI Schedule Maker is a Full Stack Web Application designed to automate the process of schedule creation for students. It includes a user-friendly interface and intelligent algorithms that effectively minimize the time required to create schedules. What once took several hours of planning and creating schedules now takes only a few seconds.

This tool is currently being used by over 1000 students at our school, making it a valuable asset for enhancing academic efficiency.

## Features

- User-friendly interface for easy schedule creation
- Intelligent algorithms that optimize schedule creation

## Technologies Used

- ReactJS for the frontend [You can find the repo here!](https://github.com/BubuDavid/DCI_hacedor_horarios_backend)
- FastAPI for the backend 

## Getting Started

### Prerequisites

- Node.js
- Python


### Installation (Backend Only)

1. Clone the repo
   ```sh
   git clone https://github.com/BubuDavid/DCI_hacedor_horarios_backend.git
   ```
2. Install Python packages
   ```sh
   python -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```

4. Create an .env file with the following variables:
   ```sh
   AIRTABLE_API_KEY = The airtable Token where is stored the database.
   AIRTABLE_BASE_ID = The airtable base id of the data.
   AIRTABLE_TABLE_NAME = The airtable name of the table witht the data
   ```

5. Start the server
   ```sh
   uvicorn main:app --reload
   ```
   

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

David Pedroza Segoviano - david.pedroza.segoviano@gmail.com

Project Link: [https://github.com/BubuDavid/DCI_hacedor_horarios_backend](https://github.com/BubuDavid/DCI_hacedor_horarios_backend)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BubuDavid/DCI_hacedor_horarios_backend.svg?style=for-the-badge
[contributors-url]: https://github.com/BubuDavid/DCI_hacedor_horarios_backend.git/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BubuDavid/DCI_hacedor_horarios_backend.svg?style=for-the-badge
[forks-url]: https://github.com/BubuDavid/DCI_hacedor_horarios_backend.git/network/members
[stars-shield]: https://img.shields.io/github/stars/BubuDavid/DCI_hacedor_horarios_backend.svg?style=for-the-badge
[stars-url]: https://github.com/BubuDavid/DCI_hacedor_horarios_backend.git/stargazers
[issues-shield]: https://img.shields.io/github/issues/BubuDavid/DCI_hacedor_horarios_backend.svg?style=for-the-badge
[issues-url]: https://github.com/BubuDavid/DCI_hacedor_horarios_backend.git/issues
[license-shield]: https://img.shields.io/github/license/BubuDavid/DCI_hacedor_horarios_backend.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/davidpedrozasegoviano/
[product-screenshot]: static/images/screenshot.png
