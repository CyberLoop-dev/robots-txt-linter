import unittest
from main import lint


class RobotsTests(unittest.TestCase):
    def test_flags_rule_before_agent(self):
        issues = lint("Disallow: /private\nUser-agent: *\nAllow: /")
        self.assertEqual(issues[0][1], "error")

    def test_flags_site_wide_block(self):
        issues = lint("User-agent: *\nDisallow: /\n")
        self.assertTrue(any("entire site" in item[2] for item in issues))

    def test_accepts_sitemap(self):
        self.assertEqual(lint("User-agent: *\nAllow: /\nSitemap: https://example.com/sitemap.xml"), [])


if __name__ == "__main__":
    unittest.main()
