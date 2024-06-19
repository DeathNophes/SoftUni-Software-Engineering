SELECT
    ph.id,
    (SELECT COUNT(*) FROM likes WHERE photo_id = ph.id) AS "likes_count",
    (SELECT COUNT(*) FROM comments WHERE photo_id = ph.id) AS "comments_count"
FROM
    photos AS ph
ORDER BY
    likes_count DESC,
    comments_count DESC,
    ph.id;
