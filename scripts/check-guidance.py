"""Validate the contribution assets before changing the inherited defaults."""
import pathlib
import re
import yaml

root = pathlib.Path(__file__).resolve().parents[1]
required = [
    'README.md', 'CONTRIBUTING.md', '.github/pull_request_template.md',
    'docs/reviewing-pull-requests.md', 'docs/github-settings-baseline.md',
    '.github/ISSUE_TEMPLATE/bug_report.yml',
    '.github/ISSUE_TEMPLATE/change_request.yml',
    '.github/ISSUE_TEMPLATE/config.yml',
]
for name in required:
    path = root / name
    assert path.is_file() and path.read_text().strip(), f'Missing guidance: {name}'

for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    content = path.read_text()
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if '://' in target or target.startswith('#'):
            continue
        target_path = (path.parent / target.split('#', 1)[0]).resolve()
        assert target_path.is_relative_to(root), f'Link escapes repository: {path.name}'
        assert target_path.exists(), f'Broken local link: {path.name}: {target}'
    assert not re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b', content), f'Possible credential in {path.name}'

for path in (root / '.github').rglob('*.yml'):
    assert isinstance(yaml.safe_load(path.read_text()), dict), f'Invalid YAML document: {path.name}'

folder = root / '.github' / 'ISSUE_TEMPLATE'
for path in folder.glob('*.yml'):
    data = yaml.safe_load(path.read_text())
    assert isinstance(data, dict), f'Invalid YAML document: {path.name}'
    if path.name == 'config.yml':
        assert isinstance(data.get('blank_issues_enabled'), bool), 'Issue configuration needs a boolean'
        continue
    assert data.get('name') and data.get('description'), f'Missing issue form identity: {path.name}'
    assert isinstance(data.get('body'), list) and data['body'], f'Missing form fields: {path.name}'
    ids = []
    for item in data['body']:
        assert item.get('type') in {'markdown', 'textarea', 'input', 'dropdown', 'checkboxes'}, f'Unknown field type: {path.name}'
        assert isinstance(item.get('attributes'), dict), f'Missing attributes: {path.name}'
        if item['type'] == 'markdown':
            assert item['attributes'].get('value'), f'Empty instructions: {path.name}'
        else:
            assert item.get('id') and item['attributes'].get('label'), f'Missing field identity: {path.name}'
            ids.append(item['id'])
    assert len(ids) == len(set(ids)), f'Duplicate issue field IDs: {path.name}'

print('Guidance files, local links, credential markers and issue forms passed.')
