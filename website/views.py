from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Member
from sqlalchemy import or_
from . import db
from flask_login import current_user

views = Blueprint('views', __name__)


@views.route('/search', methods=['GET', 'POST'])
def search():
    members = []
    search = request.args.get('search')
    if search:
        members = Member.query.filter(or_(Member.member_first.like(f"%{search}%"),
                                           Member.member_last.like(f"%{search}%"))).all()
    return render_template('search.html', members=members, user=current_user)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', user=current_user)


@views.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        member_first = request.form.get('member_first')
        member_last = request.form.get('member_last')
        member_email = request.form.get('member_email')
        member_address = request.form.get('member_address')
        category = request.form.get('category')

        member = Member.query.filter_by(member_email=member_email).first()
        if member:
            flash('Member already in database.', category='error')
        else:
            new_member = Member(member_first=member_first, member_last=member_last,
                                member_email=member_email, member_address=member_address,
                                category=category, user_id=current_user.id)
            db.session.add(new_member)
            db.session.commit()
            flash('Member added!', category='success')
        return redirect((url_for('views.home')))
    return render_template('input.html', user=current_user)