import React from 'react';
import kartItem from './KartItem.jsx';


const Kart = (props) => {
	const { items } = props;

	if (items) {
		return (
			<div className="KartItems">
				<table>
					<tr>
						<th>ITEMS</th>
						<th>QUANTITY</th>
					</tr>
						{
								items.map((item, i) => {
										return (
												<KartItem
														key={`${item.item}-${i}`}
														item={item}
												/>
										);
								})
						}
					</table>
				</div>
			);
	} else {
		return (
			<span>add some items above!</span>
		);
	}
}

export default Kart;
