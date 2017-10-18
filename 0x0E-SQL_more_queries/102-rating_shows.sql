-- List all shows and the sum of their ratings from `hbtn_0d_tvshows_rate`
SELECT tv_shows.title AS title,
       SUM(tv_show_ratings.rate) AS rating
  FROM tv_shows
       INNER JOIN tv_show_ratings
       ON tv_shows.id = tv_show_ratings.show_id
 GROUP BY tv_shows.id
 ORDER BY rating DESC;
