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

    def test_starts_a_new_group_after_rules(self):
        issues = lint("User-agent: *\nDisallow: /\nUser-agent: Googlebot\nDisallow: /private\n")
        warnings = [message for _, severity, message in issues if severity == "warning"]
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
