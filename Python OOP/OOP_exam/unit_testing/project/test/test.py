from project.social_media import SocialMedia
from unittest import TestCase, main


class TestSocialMedia(TestCase):
    ALLOWED_PLATFORMS = ['Instagram', 'YouTube', 'Twitter']

    def setUp(self) -> None:
        self.social = SocialMedia('User', 'YouTube', 100, 'Gaming')

    def test_correct_init(self):
        self.assertEqual('User', self.social._username)
        self.assertEqual('YouTube', self.social.platform)
        self.assertEqual(100, self.social.followers)
        self.assertEqual('Gaming', self.social._content_type)
        self.assertEqual([], self.social._posts)

    def test_wrong_platform_init_raises_value_error(self):
        expected_message = f"Platform should be one of {self.ALLOWED_PLATFORMS}"

        with self.assertRaises(ValueError) as ve:
            self.social1 = SocialMedia('Wrong', 'Reddit', 100, 'News')

        self.assertEqual(expected_message, str(ve.exception))

    def test_less_than_zero_followers_init(self):
        with self.assertRaises(ValueError) as ve:
            self.social.followers = -100

        expected_message = "Followers cannot be negative."

        self.assertEqual(expected_message, str(ve.exception))

    def test_create_post_expect_success(self):
        expected_message = f"New Gaming post created by User on YouTube."
        message = self.social.create_post('New game')

        self.assertEqual(expected_message, message)
        self.assertEqual([{'content': 'New game', 'likes': 0, 'comments': []}], self.social._posts)

    def test_like_post_expect_success(self):
        self.social.create_post('New game')

        expected_message = f"Post liked by User."
        message = self.social.like_post(0)

        self.assertEqual(expected_message, message)
        self.assertEqual(1, self.social._posts[0]['likes'])

    def test_like_post_expect_max_likes(self):
        self.social.create_post('New game')
        self.social._posts[0]['likes'] = 10

        expected_message = f"Post has reached the maximum number of likes."
        message = self.social.like_post(0)

        self.assertEqual(expected_message, message)
        self.assertEqual(10, self.social._posts[0]['likes'])

    def test_like_post_wrong_index_expect_error_message(self):
        self.social.create_post('New game')

        expected_message = "Invalid post index."
        message = self.social.like_post(1)

        self.assertEqual(expected_message, message)

    def test_comment_on_post_expect_success(self):
        self.social.create_post('New game')
        self.social.create_post('Old game')

        expected_message = f"Comment added by User on the post."
        message = self.social.comment_on_post(0, 'This is amazing post')
        message2 = self.social.comment_on_post(1, 'This is another amazing post')

        comments = [
            {'user': 'User', 'comment': 'This is amazing post'},
        ]
        comments2 = [
            {'user': 'User', 'comment': 'This is another amazing post'}
        ]

        self.assertEqual(expected_message, message)
        self.assertEqual(expected_message, message2)
        self.assertEqual(comments, self.social._posts[0]['comments'])
        self.assertEqual(comments2, self.social._posts[1]['comments'])

    def test_comment_on_post_expect_less_than_10_characters(self):
        self.social.create_post('New game')

        expected_message = "Comment should be more than 10 characters."
        message = self.social.comment_on_post(0, 'hahaha')

        self.assertEqual(expected_message, message)


if __name__ == '__main__':
    main()