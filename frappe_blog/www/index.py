import frappe

def get_context(context):
    context.blog = frappe.db.get_list('Blog Post',
    filters={
        'published': True
    },
    fields=['title','published_on','blog_intro', 'blogger', 'route'],
    order_by = 'published_on desc'
    )