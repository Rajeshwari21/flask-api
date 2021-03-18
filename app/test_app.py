import unittest
import json
import app

BASE_URL = 'http://localhost:5000/v1/sanitized/input/'

# Class InputValidation


class InputValidationTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    # Tests for unsanitized input.
    def test_input_unsanitized(self):
        input_1 = {
            "payload": "Dummy Content can place dummy text into your article via two alternative methods: direct content, and dynamic tag You can use the dedicated Editor Button to enter any of the two methods.; 1+AND+IF(version()+LIKE+'5 % ', sleep(5), false; Dummy Content can place dummy text into your article via two alternative methods: direct content, and dynamic tag. You can use the dedicated Editor Button to enter any of the two methods."
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_1),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'unsanitized', response.data)

        input_2 = {
            "payload": "The scenario above indicates that a blind SQL Injection attack is possible. The scenario above indicates that a blind SQL Injection attack is possible. The scenario above indicates that a blind SQL Injection attack is possible.;'RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='; Moving forward with identifying the number of columns, we use the following payload Moving forward with identifying the number of columns,;admin') or ('1'='1'--; we use the following payload Moving forward with identifying the number of columns, we use the following payload Moving forward with identifying the number of columns, we use the following payload"
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_2),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'unsanitized', response.data)

        input_3 = {
            "payload": "You can use this WordPress dummy data generator to easily generate blog posts, pages, import images, and more. Following are a few scenarios where you may find this dummy data very useful You can use this WordPress dummy data generator to easily generate blog posts, pages, import images, and more. Following are a few scenarios where you may find this dummy data very useful;1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055; Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty;UNION ALL SELECT NULL#; WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content"
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_3),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'unsanitized', response.data)

        input_4 = {
            "payload": "Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content; ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8,9,10,11,12#; This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content."
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_4),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'unsanitized', response.data)

        input_5 = {
            "payload": "Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content.Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content. Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content Adding dummy content allows you to fill up an empty WordPress site with placeholder content. This allows you to see how a website will look and how your plugins would work with content"
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_5),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'unsanitized', response.data)

     # Tests for sanitized input.
    def test_input_sanitized(self):
        input_1 = {
            "payload": "Dummy Content is a Joomla system plugin and editor button that helps you automatically place random dummy text into your Articles or in any other content item that has an editor, such as Custom HTML Modules, Category descriptions, 3rd party content, etc."
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_1),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sanitized', response.data)

        input_2 = {
            "payload": "With this method, Dummy Content will then replace that tag in the frontend with a dynamically generated dummy text.The editor button will automatically generate the appropriate tag based on your specified Content Type and Options in the editor button popup. But you are also free to enter the tag manually. Here is a quick rundown on how the tag syntax works:"
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_2),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sanitized', response.data)

        input_3 = {
            "payload": "With this method, Dummy Content will then replace that tag in the frontend with a dynamically generated dummy text.The editor button will automatically generate the appropriate tag based on your specified Content Type and Options in the editor button popup. But you are also free to enter the tag manually. Here is a quick rundown on how the tag syntax works:"
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_3),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sanitized', response.data)

        input_4 = {
            "payload": "In the Pro version of Dummy Content you can also generate dummy images, with the given width and height.There are a range of online dummy image services you can choose from. Each have different options, like text overlays, photo categories, color schemes, foreground and background colors."
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_4),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sanitized', response.data)

        input_5 = {
            "payload": ""
        }
        response = self.app.post(BASE_URL, data=json.dumps(input_5),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sanitized', response.data)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
