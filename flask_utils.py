from flask import Flask, render_template, abort, send_file, request, jsonify, redirect, make_response


def get_args(req) -> dict:
    """
    Obtain in a dict all args from: form and args
    """
    result: dict = {}
    if req.args.__len__() > 0:
        result.update(req.args)
    if req.form.__len__() > 0:
        result.update(req.form)
    return result


def prepare_cookie_and_template(url: str, cookie_key: str, cookie: str, expire: bool) -> request:
    # Le enviamos el index
    resp = make_response(render_template(url))
    if cookie.__len__() > 0 and cookie_key.__len__() > 0:
        # Le enviamos la cookie de sesion
        if expire:
            resp.set_cookie(cookie_key, cookie, httponly=True, expires=0)
        else:
            resp.set_cookie(cookie_key, cookie, httponly=True)
    return resp




