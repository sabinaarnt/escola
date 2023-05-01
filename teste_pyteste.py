import requests

class TestCursos:
    headears = { 'Authorization': 'Token 12f172cd244d8f47040debf25e93492dc2c33487' }
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headears)

        assert cursos.status_code == 200

    def test_get_curso(self):
        cursos = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headears)

        assert cursos.status_code == 200


        