from Tag import Tag


class TagHandler:

    def __init__(self):
        self.tag = {}

    def get_tags(self):
        return self.tag.values()

    def get_tag(self, name):
        return self.tag[name] if name in self.tag else None

    def add_tag(self, tag_name, tag_description, field_name):
        if tag_name in self.tag:
            return False
        else:
            self.tag[tag_name] = Tag(tag_name, tag_description, field_name)
            return True

    def delete_tag(self, name):
        if name in self.tag:
            del self.tag[name]
            return True
        else:
            return False

    def update_tag(self, old_name, new_name, new_field_name, new_description):
        if old_name in self.tag and (new_name == old_name or new_name not in self.tag):
            single_tag = self.tag[old_name]
            single_tag.set_name(new_name)
            single_tag.set_field_name(new_field_name)
            single_tag.set_description(new_description)
            self.delete_tag(old_name)
            self.tag[new_name] = single_tag
            return True
        else:
            return False
