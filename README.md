# Developing with Nondeterministic APIs
This is the repository for the LinkedIn Learning course `Developing with Nondeterministic APIs`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

AI APIs produce nondeterministic output meaning the same prompt may produce different results every time it’s run. This poses unique challenges to developers because traditional software development is based on the premise that systems produce consistent and therefore deterministic outputs. In this course you’ll learn strategies for how to mitigate these unique challenges to meld traditional software development with modern AI tools.

_See the readme file in the main branch for updated instructions and information._

## Instructions
This repository provides basic examples of how to introduce greater determinism and consistency to the responses from the OpenAI API.

The examples are demonstrated in the course and provided as-is. They are not meant as a follow-along exercise but rather for reference and further experimentation.

The examples are named for the chapter and video number they appear in. Each example is stand-alone and runs in terminal.

To use these exercise files you need an OpenAI API key. You get that key at [platform.openai.com](https://platform.openai.com)

## Running the examples in GitHub Codespaces
1. Click the "Code" button and select "Codespaces."
2. Create a new Codespace or open one you've already created.
3. Create a new file named `.env` in the root folder.
4. Add `OPENAI_API_KEY=` followed by your OpenAI API key to `.env`
5. Note `.env` is not tracked by GitHub so the file will only exist in this Codespace.
6. To run the Python example in terminal, use the `python [filename].py` command.

### Instructor

Morten Rand-Hendriksen 
                            
Developer and Senior Staff Instructor

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/morten-rand-hendriksen).

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4D0DAQGuS08YZgxSZw/learning-public-crop_675_1200/0/1707772825785?e=2147483647&v=beta&t=iRDlEZbLCunOM4D2YMCUQDF_PU1hrWNsuHH1jlM0tZ8

